pipeline{
	agent any
	stages{
	    stage('Instalción'){
			steps{
			    echo "apt-get update"
				echo "apt-get install python3 python3-pip"
				echo "pip install virtualenv"
				echo "virtualenv entorno"
				echo "source entorno/bin/activate"
				echo "pip install -r requirements.txt"
			}
		}
		stage('Verificación de código'){
			steps{
				echo "Verifica estándar de código"
				echo "Verifica complejidad ciclomática"
			}
		}
		stage('Testing'){
			steps{
				echo "Ejecución de pruebas unitarias"
				echo "Ejecución de pruebas de aceptación"
				echo "Verfica coverage"
			}
		}
		stage('Build'){
			steps{
				echo "Crea el arvhivo .war"
			}
		}
		stage('Servidor de pre-producción'){
			steps{
				echo "Copia la aplicación al servidor de pruebas"
			}
		}
		stage('Servidor de producción'){
			input{
			        message "Quieres hacer el despligue a producción?"
			        ok "Si"
			}
			steps{
				echo "Copia la aplicación al servidor de producción"
			}
		}
	}
}
chuckNorris()
