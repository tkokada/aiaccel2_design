FROM mongo

COPY users.json /init.json

CMD mongoimport --drop --host mongo --db user --collection user --mode delete --type json --file /init.json --jsonArray


CMD mongoimport --drop --host mongo --db user --collection user --type json --file /init.json --jsonArray
