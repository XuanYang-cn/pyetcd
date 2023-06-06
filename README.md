# pyetcd

[![version](https://img.shields.io/pypi/v/etcd-sdk-python.svg?color=blue)](https://pypi.org/project/etcd-sdk-python/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/etcd-sdk-python?logo=python&logoColor=blue)](https://pypi.org/project/etcd-sdk-python/)
[![Downloads](https://pepy.tech/badge/etcd-sdk-python)](https://pepy.tech/project/etcd-sdk-python)
[![Downloads](https://pepy.tech/badge/etcd-sdk-python/month)](https://pepy.tech/project/etcd-sdk-python/month)
[![license](https://img.shields.io/hexpm/l/plug.svg?color=green)](https://github.com/xuanyang-cn/pyetcd/blob/main/LICENSE)

Python client for the etcd API v3, supported python >= 3.7, under active maintenance

## Install
```shell
pip install etcd-sdk-python
```
## Road maps and TODOs

### Road maps
|version|release date|target|status|
|:-----:|:----------:|------|:----:|
|0.0.1  |Apr 10,2023 |enable >= python3.7|DONE  |
|0.0.2  |Jun 6,2023 ||DONE|
|0.0.3  |ND |set up github actions, run pass unittests, set up merging rules, ensure quality|WIP|


### TODOs for v0.0.2
|functions|version|status|
|---------|:-----:|:----:|
|make ut work|0.0.2|BACKLOG|
|make tox.ini work|0.0.2|BACKLOG|
|enable running ut for pull requests|0.0.2|BACKLOG|
|enable running lint for pull requests|0.0.2|BACKLOG|
|enable publishing dev packages for merge|0.0.2|BACKLOG|
|Add mergify to help merging PRs|0.0.2|BACKLOG|


## Basic usage:

```python
import pyetcd

etcd = pyetcd.client()

etcd.get('foo')
etcd.put('bar', 'doot')
etcd.delete('bar')

# locks
lock = etcd.lock('thing')
lock.acquire()
# do something
lock.release()

with etcd.lock('doot-machine') as lock:
    # do something

# transactions
etcd.transaction(
    compare=[
        etcd.transactions.value('/doot/testing') == 'doot',
        etcd.transactions.version('/doot/testing') > 0,
    ],
    success=[
        etcd.transactions.put('/doot/testing', 'success'),
    ],
    failure=[
        etcd.transactions.put('/doot/testing', 'failure'),
    ]
)

# watch key
watch_count = 0
events_iterator, cancel = etcd.watch("/doot/watch")
for event in events_iterator:
    print(event)
    watch_count += 1
    if watch_count > 10:
        cancel()

# watch prefix
watch_count = 0
events_iterator, cancel = etcd.watch_prefix("/doot/watch/prefix/")
for event in events_iterator:
    print(event)
    watch_count += 1
    if watch_count > 10:
        cancel()

# recieve watch events via callback function
def watch_callback(event):
    print(event)

watch_id = etcd.add_watch_callback("/anotherkey", watch_callback)

# cancel watch
etcd.cancel_watch(watch_id)

# recieve watch events for a prefix via callback function
def watch_callback(event):
    print(event)

watch_id = etcd.add_watch_prefix_callback("/doot/watch/prefix/", watch_callback)

# cancel watch
etcd.cancel_watch(watch_id)
```

## Credits

Many thx to  [python-etcd3](https://github.com/kragniz/python-etcd3)
