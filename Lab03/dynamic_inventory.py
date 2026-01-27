#!/usr/bin/env python3
import json
inventory = {
    "web_servers": {
        "hosts": ["managed_node01"],
        "vars": {
           "ansible_host": "192.168.25.2",
           "ansible_user": "ayong2"
        }
    },
    "db_servers": {
        "hosts": ["managed_node02"],
        "vars": {
            "ansible_host": "192.168.25.3",
            "ansible_user": "ayong2"
        }
    }
}
def main():
    print(json.dumps(inventory))

if __name__ == "__main__":
      main()
