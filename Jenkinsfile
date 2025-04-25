pipeline {
    agent none
    stages {
        stage('Matrix Test') {
            matrix {
                axes {
                    axis {
                        name 'PY_VER'
                        values 'python3.10', 'python3.11'
                    }
                }
                agent { label 'local' }
                environment {
                    PATH = "${env.HOME}/.pyenv/shims:${env.PATH}"
                }
                stages {
                    stage('Install & Test') {
                        steps {
                            sh """ 
                                ${PY_VER} -m pip install -q --upgrade pip
                                pip3 install -q -r requirements.txt
                                pytest -q
                            """
                        }
                    }
                }
            }


        }
    }
}