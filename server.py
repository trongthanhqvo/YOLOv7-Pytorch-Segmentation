from waitress import serve
import app
print("Server Started On Port 8081") 
serve(app.app, host='0.0.0.0', port=8081, threads=6)
