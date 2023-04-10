=========
API Usage
=========

To use pyetcd in a project:

.. code-block:: python

    import pyetcd

and create a client:

.. code-block:: python

    etcd = pyetcd.client()

This defaults to localhost, but you can specify the host and port:

.. code-block:: python

    etcd = pyetcd.client(host='etcd-host-01', port=2379)

If you would like to specify options for the underlying GRPC connection, you can also pass it as a parameter:

.. code-block:: python

    etcd = pyetcd.client(grpc_options={
                            'grpc.http2.true_binary': 1,
                            'grpc.http2.max_pings_without_data': 0,
                        }.items())

Putting values into etcd
------------------------

Values can be stored with the ``put`` method:

.. code-block:: python

    etcd.put('/key', 'dooot')

You can check this has been stored correctly by testing with etcdctl:

.. code-block:: bash

    $ ETCDCTL_API=3 etcdctl get /key
    /key
    dooot

API
===

.. autoclass:: pyetcd.MultiEndpointEtcd3Client
    :members:

.. autoclass:: pyetcd.Etcd3Client
    :members:

.. autoclass:: pyetcd.Endpoint
    :members:

.. autoclass:: pyetcd.Member
    :members:

.. autoclass:: pyetcd.Lease
    :members:

.. autoclass:: pyetcd.Lock
    :members:
