#!/usr/bin/python

from pymongo import MongoClient

client = MongoClient('localhost:27117')
db = client.dorry

result1 = db.imageconfig.insert_one(
    {
        "imageId":"sha256:baa5d63471ead618ff91ddfacf1e2c81bf0612bfeb1daf00eb0843a41fbfade3",
        "config":{
            "Tty": True,
            "Image": "baa5d63471ead618ff91ddfacf1e2c81bf0612bfeb1daf00eb0843a41fbfade3",
            "Cmd": ["/bin/sh"]
        }
    }
)
print result1

result2 = db.imageconfig.insert_one(
    {
        "imageId":"sha256:965940f98fa591b5a98d0d7063de58f9fb04f79f0a6a1046c25f971416130d88",
        "config":{
            "Tty": True,
            "Image": "965940f98fa591b5a98d0d7063de58f9fb04f79f0a6a1046c25f971416130d88",
            "HostConfig": {
                "Binds": ["/var/run/docker.sock:/var/run/docker.sock"],
                "PortBindings": { "9000/tcp": [{ "HostPort": "9000" }] },
                "Privileged": True,
            }
        }
    }
)
print result2

result3 = db.imageconfig.insert_one(
    {
        "imageId":"sha256:b85cb2cf09349e6858d9f24fe045a73c0ccb7b29ed740510b8b96bab2993bd70",
        "config":{
            "Tty": True,
            "Image": "b85cb2cf09349e6858d9f24fe045a73c0ccb7b29ed740510b8b96bab2993bd70",
            "HostConfig": {
                "Binds": [
                    "/dorry_data/samba/share/:/data/",
                    "/dorry_data/samba/backup/:/home/backup/"
                ],
                "PortBindings": { "445/tcp": [{ "HostPort": "445" }] },
            }
        }
    }
)
print result3

result4 = db.imageconfig.insert_one(
    {
        "imageId":"sha256:8ad386ec89973f4e26c051e67823094c329208dd4005435e3d713b4379012cda",
        "config":{
            "Tty": True,
            "Image": "8ad386ec89973f4e26c051e67823094c329208dd4005435e3d713b4379012cda",
            "HostConfig": {
                "Binds": [
                    "/etc/localtime:/etc/localtime",
                    "/dorry_data/samba/share/:/data/",
                    "/dorry_data/samba/backup/:/home/backup/"
                ],
            }
        }
    }
)
print result4
