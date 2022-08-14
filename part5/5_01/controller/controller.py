from time import sleep
from kubernetes import client, config
import json


def receive_dummysite():
    api_client = client.ApiClient()
    #response = api_client.call_api('/apis/stable.dwk/v1/dummysites', 'GET', response_type='json')
    ret_metrics = api_client.call_api('/apis/stable.dwk/v1/dummysites', 'GET', auth_settings = ['BearerToken'], response_type='json', _preload_content=False) 
    response = ret_metrics[0].data.decode('utf-8')
    dict_response = json.loads(response)

    image = dict_response['items'][0]['spec']['image']
    url = dict_response['items'][0]['spec']['website_url']

    return image, url
    

def create_job(image, url):
    api_client = client.BatchV1Api()

    job_template = {
        "apiVersion": "batch/v1",
        "kind": "Job",
        "metadata": { "name": "dummysite-job"},
        "spec": {
            "template": {
                "spec": {
                    "containers": [{
                        "name": "dummysite",
                        "image": image,
                        "ports": [{"containerPort": 5000}],
                        "env": [{
                            "name": "URL",
                            "value": url,
                        }]
                    }],
                    "restartPolicy": "Never"
                }
            },
            "backoffLimit": 4
        }
    }

    response = api_client.create_namespaced_job(
        body=job_template,
        namespace="default")
    print('Job created')


def create_deployment(image, url):
    apps_v1 = client.AppsV1Api()

    deployment_template = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": 'dummysite-dep'},
        "spec": {"replicas": 1,
                "selector": {
                    "matchLabels": {
                        "app": "dummysite"
                    }},
            "template": {"metadata": {"labels": {"app": "dummysite"}},
                "spec": {"containers": [
                    {"name": "dummysite", "image": image, "ports": [{"containerPort": 5000}], 'env': [{'name': 'URL', 'value': url}]}]
                }
            },
        }
    }

    # Create deployement
    resp = apps_v1.create_namespaced_deployment(
        body=deployment_template, namespace="default"
    )

    print('\n[INFO] deployment `dummysite-deployment` created.\n')
    print(
        f'''
        NAMESPACE: {resp.metadata.namespace}  
        NAME: {resp.metadata.name}  
        REVISION: {resp.metadata.generation}  
        IMAGE: {resp.spec.template.spec.containers[0].image}
        '''
    )



def create_service():
    core_v1_api = client.CoreV1Api()

    service_template = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"name": 'dummysite-svc'},
        "spec": {"type": 'NodePort',
                "selector": {
                    "app": "dummysite"
                },
            "ports": [{
                "name": 'http',
                'protocol': 'TCP',
                'port': 5432,
                'targetPort': 5000
            }],
        },
    }

    resp = core_v1_api.create_namespaced_service(
        namespace="default", 
        body=service_template
    )

    print('\n[INFO] service `dummysite-svc` created.\n')
    print(
        f'''
        NAMESPACE: {resp.metadata.namespace}  
        NAME: {resp.metadata.name}  
        REVISION: {resp.metadata.generation}  
        '''
    )


def create_ingress():
    networking_v1_api = client.NetworkingV1Api()

    ingress_template = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "Ingress",
        "metadata": {"name": 'dummysite-ingress'},
        "spec": {
            'rules': [{
                'paths': {
                    'path': '/',
                    'pathType': 'Prefix',
                    'dummysite': {
                        'service': 'dummysite-svc',
                        'port': {
                            'number': 5432
                        }
                    }
                }
            }]
        },
    }
        
    resp = networking_v1_api.create_namespaced_ingress(
        namespace="default",
        body=ingress_template
    )

    print('\n[INFO] ingress `dummysite-ingress` created.\n')
    print(
        f'''
        NAMESPACE: {resp.metadata.namespace}  
        NAME: {resp.metadata.name}  
        REVISION: {resp.metadata.generation}  
        '''
    )


def main():
    #config.load_kube_config()
    config.load_incluster_config()

    image, url = receive_dummysite()

    #try:
    #    create_job(image, url)
    #except:
    #    print('job already exists')    

    try:
        create_deployment(image, url)
    except:
        print('deployment already exists')
    
    try:
        create_service()
    except:
        print('service already exists')

    try:
        create_ingress()
    except:
        print('ingress already exists')
    sleep(60)

if __name__ == '__main__':
    main()