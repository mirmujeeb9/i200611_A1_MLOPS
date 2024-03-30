pipeline {
  agent any

  stages {
    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("mirmujeeb9/i200611_a1_mlops")
        }
      }
    }
    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('', 'dockerhub') {
            dockerImage.push("latest")
            dockerImage.push("${env.BUILD_ID}")
          }
        }
      }
    }
  }

  post {
    success {
      mail to: 'mirmujeebahmed15@gmail.com',
           subject: "MLOPS EMAIL- Build ${env.BUILD_ID}",
           body: "jenkins has run"
    }
    failure {
      mail to: 'mirmujeebahmed15@gmail.com',
           subject: "MLOPS EMAIL BUILD ${env.BUILD_ID}",
           body: "failed to push jenkins"
    }
  }
}
