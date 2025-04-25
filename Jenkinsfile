pipeline {
  agent none

  stages {
    stage('Matrix Test') {
      matrix {
        axes {
          axis {
            name 'PY_VER'
            values '3.10','3.11'          // 先单版本跑通，再加 '3.10'
          }
        }
        agent { label 'local' }

        environment {
          PATH = "/usr/local/bin:/usr/local/opt/python@3.11/bin:/bin:/usr/bin:${env.PATH}"
        }

        stages {
          stage('Install & Test') {
            steps {
              sh '''
                echo "Running on Python $(python3 -V)"
                python3 -m pip install --upgrade pip
                pip install -r requirements.txt
                pytest -q
              '''
            }
          }
        }
      }
    }
  }
}
