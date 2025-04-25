pipeline {
  agent none                          // 顶层无 agent
  environment {
    PATH = "/usr/local/bin:/usr/local/opt/python@3.11/bin:${env.PATH}"
  }

  stages {
    stage('Matrix Test') {
      parallel {
        stage('py310') {              // ❶
          agent { label 'local' }
          steps {
            sh '''
              pyenv global 3.10
              python3 -m pip install --upgrade pip
              pip3 install -r requirements.txt
              pytest -q
            '''
          }
        }
        stage('py311') {              // ❷
          agent { label 'local' }
          steps {
            sh '''
              pyenv global 3.11
              python3 -m pip install --upgrade pip
              pip3 install -r requirements.txt
              pytest -q
            '''
          }
        }
      }
    }
  }
}
