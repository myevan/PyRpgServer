%~dp0venv.bat locust -f %~dp0main_locust.py --web-host localhost --web-port 9000 --host http://localhost:8000 -u 10 -r 10 -t 1m --autostart