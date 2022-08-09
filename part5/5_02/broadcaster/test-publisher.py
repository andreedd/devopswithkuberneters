# https://docs.nats.io/using-nats/developer/sending

import asyncio
from nats.aio.client import Client as NATS

nc = NATS()


async def main():
  """Publishes msg to local nats"""
  await nc.connect(servers=["nats://localhost:4222"])

  print('sending msg')
  await nc.publish("updates", b'All is Well')
  print('msg sent')

  return

if __name__ == '__main__':
  asyncio.run(main())
