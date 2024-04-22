from flask import Flask, render_template, request
import boto3

app = Flask(__name__)

# Define the region and endpoint name
region_name = 'us-east-1'
endpoint_name = 'xgboost-2024-04-21-15-54-11-914'

# Use the provided AWS credentials
aws_access_key_id = 'ASIAUYYOMVIYPIOBHRWJ'
aws_secret_access_key = 'mvtuAUt/vP729BIRuzpx1lrfy9q+z6PtJ1DjxU3E'
aws_session_token = 'IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICh90ZWH02PmwUWLxmixdZo7/XEolezKltIGskeD+7XrAiB8lTTDH1I6uBRipSGdDtZLi51XDnCdW+/pj//ms8KIxiq6AghhEAEaDDMyODA1ODMxNzM2MCIMn+YPxSNeVA6qBY4MKpcCRjlf6jvjWioE59q4ujpj1GAnKnO9dcoDOrSVc0czWNzrBpKLkym/0OtLv3Hpha/brAg50v+Dk76MEjoxD80ElWS8+ieREQp1IssO7nLiZRvPreQoGJyccFK5Ckhy7kW/ioscWqjqqNVxeUJLjtuS8tu19RV6w3yOYEEeWqboRGIZIBSyA8e6T68ljrOHtoiMfQ6r2rDYmiEDRhrVLvcyo0VwjFvASmwt3sxOiTThiTYsBxZKBg5Lc2PaBsv4NWDu6mFS0EXOOSsLcRmtCDd5TgGaxZXT36Vcgtn9QT5zTKUQ0QIv04pr6G+3FUeFmwxaTJRAAuv2T/LcCTikjZE5Id/SzFBgxMVa+E8ujEmgdWsBCAFoI+RgMKmLmrEGOp4B7m2cl3bNScEbmJzmddCnw9re1jHf7ZbpGocF65Xtb4tLb0Lr72+H8/CCJTzSPr8BolEd47aXdmd+8Mff/ocL6aSE4mkhUcFpyQAZr8wFXKuPcAWyGDdxm0coF6rjYiC9Fej+5rYJyhqAx6IMMxA3jVODdurspbJvhpWOVcvtAnmau5waGqQLFm2+xPkGcYQuTDNvZPnX7UhEw6raYxI='
aws_region = 'us-east-1'
# Create a Boto3 session with the provided credentials and region
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=region_name
)

# Create a Boto3 client for SageMaker
sagemaker_runtime = session.client('sagemaker-runtime')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    data = request.form['data']

    # Make a prediction using the deployed model
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/csv',
        Body=data.encode('utf-8')
    )
    
    # Read the prediction response
    prediction = response['Body'].read().decode('utf-8')

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
