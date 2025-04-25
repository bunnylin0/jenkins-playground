pipeline {
    agent None
    stages {
        stage('Matrix Test') {
            matrix {
                axes {
                    axis {
                        name 'PY_VER'
                        values '3.10', '3.11'
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
                                pyenv local ${PY_VER}
                                python3 -m pip install -q --upgrade pip
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