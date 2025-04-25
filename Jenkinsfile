pipeline {
    agent { label 'local'}
    envirment {
        // 万无一失地确保用新 pip
        PATH = "/usr/local/bin:/usr/local/opt/python@3.11/bin:${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install deps & Test') {
            steps {
                sh '''
                    python3 -V
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                    pytest -q
                '''
            }
        }
    }
}
