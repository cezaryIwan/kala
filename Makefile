start: start-docker start-client start-server

start-docker:
	cd docker && sudo docker-compose up -d

start-client:
	cd client && pnpm run dev &

start-server:
	cd server && uvicorn main:app --host 0.0.0.0 --port 8000 --reload