import spotipy.util as util
token=util.prompt_for_user_token('kapilkalra','playlist-modify-private',
                           client_id='01e4ef84a877453e8b4f711e15ee4951',
                           client_secret='2faaaf0f2f3d4a0584540d889d735c19',
                           redirect_uri='http://localhost:80')
print(token)
