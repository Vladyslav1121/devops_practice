#!/bin/bash
tar -zcvf backup/backup_$(date +%m-%d-%Y).tar.gz $1
ls 
cd ~ 