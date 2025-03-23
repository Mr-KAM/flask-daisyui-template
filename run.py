import os
from app import app

#----------------------------------------
# launch code
#----------------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
	# app.run(debug=True, use_reloader=True)
