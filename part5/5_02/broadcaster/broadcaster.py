#!/usr/bin/env python3

import asyncio
from nats.aio.client import Client as NATS
import requests
import os

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
NATS_URL = os.getenv('NATS_URL')


def broadcast_to_telegram(msg):
  """broadcast the status to telegram"""
  requests.post(WEBHOOK_URL, json={'text': msg.data.decode()})
  print('todo status sent')


async def run():
    nc = NATS()

    await nc.connect(servers=[os.getenv('NATS_URL')])

    async def help_request(msg):
      print(f'msg here: {msg}')
      broadcast_to_telegram(msg)

    await nc.subscribe("updates", "workers", help_request)

    print("Listening on 'updates' ...")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.run_forever()
    loop.close()
  