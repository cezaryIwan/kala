start: start-docker start-client start-server

start-docker:
	cd docker && sudo docker-compose up -d

start-client:
	cd vue && pnpm run dev &

start-server:
	cd fastapi && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
