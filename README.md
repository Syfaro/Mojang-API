Mojang-API
==========

A Python 2 library for the Mojang API services 

## Usage

```python
from mojangapi import MojangAPI


api = MojangAPI()

status = api.service_statuses()
news = api.mojang_news()
uuid = api.get_uuid('syfaro')
```
