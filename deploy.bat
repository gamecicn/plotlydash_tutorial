
rm deploy.zip

pip freeze > requirements.txt

zip deploy.zip requirements.txt application.py ./data/*

eb deploy 

rm deploy.zip






















