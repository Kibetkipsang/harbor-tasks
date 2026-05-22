#!/bin/bash

sed -i 's/datetime.fromtimestamp/datetime.utcfromtimestamp/' /app/auth.py