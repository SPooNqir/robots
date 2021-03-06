import os
import sys
import grpc
from flask import g

import opentracing
from grpc_opentracing import open_tracing_client_interceptor
from grpc_opentracing.grpcext import intercept_channel

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

from robots_pb2_grpc import robotsStub
from robots_pb2 import Robot

class SvcRobots():
  def __init__(self, url):
    print("connect to robots svc")
    channel = grpc.insecure_channel(url) # os.environ['ROBOTS_URL']
    interceptor = open_tracing_client_interceptor(opentracing.tracer)
    channel = intercept_channel(channel, interceptor)
    self.stub = robotsStub(channel)
    print("connected :-)")

  def GetPaths(self, bearer, identity):
    metadata = (('authorization', bearer),
            ('some-md-key', 'another value'))
    rbt = self.stub.Get(request=Robot(email=identity), metadata=metadata)
    print(rbt)
    if rbt.id == 0:
      return [], False
    return rbt.paths, True
