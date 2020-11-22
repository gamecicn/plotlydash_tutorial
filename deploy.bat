
# Add following to .elasticbeanstalk/config before execute
#branch-defaults:
#  emotional_analysis_demo:
#    environment: EmotionAnalysisDemo-env
#    group_suffix: null
#deploy:
#  artifact: deploy.zip
 

rm deploy.zip

pip freeze > requirements.txt

zip deploy.zip requirements.txt application.py 

eb deploy 

rm deploy.zip






















