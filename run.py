from api import app
# import os
# PORT = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
  app.run(host="0.0.0.0", port=80,debug=True)
# app.run(host="0.0.0.0", port=PORT,debug=False)
