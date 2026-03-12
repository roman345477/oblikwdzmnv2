2026-03-12T17:26:19.330761981Z [inf]  Starting Container
2026-03-12T17:26:19.551637818Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:19.551648608Z [err]      self.load_wsgi()
2026-03-12T17:26:19.551654359Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:19.551660522Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:19.551665571Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:19.551671631Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:19.551676827Z [err]      self.callable = self.load()
2026-03-12T17:26:19.551681890Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:19.551686153Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:19.551717382Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:19.551722764Z [err]      І `Procfile`:
2026-03-12T17:26:19.551728068Z [err]        ^
2026-03-12T17:26:19.551734441Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:19.551739417Z [err]  [2026-03-12 17:26:18 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:19.551745527Z [err]  [2026-03-12 17:26:18 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:19.551753456Z [err]  [2026-03-12 17:26:18 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:19.551759500Z [err]  [2026-03-12 17:26:18 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:19.551776660Z [err]  [2026-03-12 17:26:18 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:19.551782616Z [err]  [2026-03-12 17:26:18 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:19.551788845Z [err]  Traceback (most recent call last):
2026-03-12T17:26:19.551795368Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:19.551801023Z [err]      worker.init_process()
2026-03-12T17:26:19.553237262Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:19.553242621Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.553247625Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:19.553252140Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:19.553258821Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.553264442Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:19.553270506Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:19.553274938Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.553279462Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:19.553284121Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:19.553289235Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.553300723Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:19.553306051Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:19.553311363Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:19.553316034Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:19.553320981Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:19.553325115Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:19.553329352Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:19.553341321Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:19.554553129Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:19.554557820Z [err]      І `Procfile`:
2026-03-12T17:26:19.554562280Z [err]        ^
2026-03-12T17:26:19.554568781Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:19.554574353Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:19.554578835Z [err]  [2026-03-12 17:26:18 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:19.554583103Z [err]  [2026-03-12 17:26:18 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:19.554589393Z [err]  [2026-03-12 17:26:18 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:19.554593610Z [err]  [2026-03-12 17:26:18 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:19.645896894Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:19.645903187Z [err]      І `Procfile`:
2026-03-12T17:26:19.645910044Z [err]        ^
2026-03-12T17:26:19.645915830Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:19.743081914Z [err]  [2026-03-12 17:26:19 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:19.743088197Z [err]  [2026-03-12 17:26:19 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:19.743095265Z [err]  [2026-03-12 17:26:19 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:19.762311542Z [err]  [2026-03-12 17:26:19 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:19.763931470Z [err]  [2026-03-12 17:26:19 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:19.770270142Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:19.770283044Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.770304360Z [err]  [2026-03-12 17:26:19 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:19.770307164Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:19.770315343Z [err]  Traceback (most recent call last):
2026-03-12T17:26:19.770315704Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:19.770322766Z [err]      self.callable = self.load()
2026-03-12T17:26:19.770326381Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:19.770329611Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:19.770335041Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:19.770337126Z [err]      worker.init_process()
2026-03-12T17:26:19.770340776Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:19.770345788Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.770348259Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:19.770351701Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:19.770358646Z [err]      self.load_wsgi()
2026-03-12T17:26:19.770358813Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:19.770367563Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.770369060Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:19.770375365Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:19.770378166Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:19.772495504Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:19.772503194Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:19.772509744Z [err]  [2026-03-12 17:26:19 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:19.772516349Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:19.772525891Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:19.772533894Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:19.772540980Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:19.772547998Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:19.772555224Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:19.772562302Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:19.772569318Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:19.772576109Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:19.772582597Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:19.772589324Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:19.772596345Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:19.772602536Z [err]      І `Procfile`:
2026-03-12T17:26:19.772608965Z [err]        ^
2026-03-12T17:26:19.831167366Z [err]  [2026-03-12 17:26:19 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:19.833454696Z [err]  [2026-03-12 17:26:19 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:19.833463236Z [err]  [2026-03-12 17:26:19 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:20.634592282Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:20.634597670Z [err]      І `Procfile`:
2026-03-12T17:26:20.634603250Z [err]        ^
2026-03-12T17:26:20.634607996Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:20.640430089Z [err]  [2026-03-12 17:26:20 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:20.640443341Z [err]  [2026-03-12 17:26:20 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:20.640515946Z [err]  [2026-03-12 17:26:20 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:20.657917419Z [err]  [2026-03-12 17:26:20 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:20.660449450Z [err]  [2026-03-12 17:26:20 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:20.667241203Z [err]  [2026-03-12 17:26:20 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:20.667251919Z [err]  Traceback (most recent call last):
2026-03-12T17:26:20.667260288Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:20.667267387Z [err]      worker.init_process()
2026-03-12T17:26:20.667276818Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:20.667284445Z [err]      self.load_wsgi()
2026-03-12T17:26:20.667291227Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:20.667298209Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:20.667305516Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:20.667312405Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:20.667319386Z [err]      self.callable = self.load()
2026-03-12T17:26:20.667327668Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:20.667334830Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:20.667341433Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:20.667350173Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:20.667356914Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:20.667364490Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:20.667371468Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:20.667378385Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:20.667385240Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:20.667392343Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:20.669703036Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:20.669704903Z [err]      І `Procfile`:
2026-03-12T17:26:20.669710941Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:20.669714377Z [err]        ^
2026-03-12T17:26:20.669717570Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:20.669722203Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:20.669724810Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:20.669730791Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:20.669731850Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:20.669736706Z [err]  [2026-03-12 17:26:20 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:20.669739203Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:20.669743596Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:20.669749155Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:20.669753385Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:20.669758677Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:20.669764721Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:20.669769053Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:20.733723554Z [err]  [2026-03-12 17:26:20 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:20.735506950Z [err]  [2026-03-12 17:26:20 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:20.735513397Z [err]  [2026-03-12 17:26:20 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:21.606762026Z [err]      self.callable = self.load()
2026-03-12T17:26:21.606763898Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:21.606774385Z [err]      self.load_wsgi()
2026-03-12T17:26:21.606782743Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:21.606787101Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:21.606794172Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:21.606797327Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:21.606803986Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:21.606812514Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:21.606813859Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:21.606821392Z [err]      І `Procfile`:
2026-03-12T17:26:21.606828217Z [err]        ^
2026-03-12T17:26:21.606834761Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:21.606842201Z [err]  [2026-03-12 17:26:21 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:21.606850496Z [err]  [2026-03-12 17:26:21 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:21.606851280Z [err]  [2026-03-12 17:26:21 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:21.606860668Z [err]  [2026-03-12 17:26:21 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:21.606863050Z [err]  [2026-03-12 17:26:21 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:21.606869876Z [err]  [2026-03-12 17:26:21 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:21.606878322Z [err]  Traceback (most recent call last):
2026-03-12T17:26:21.606884472Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:21.606890221Z [err]      worker.init_process()
2026-03-12T17:26:21.608401295Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:21.608407441Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:21.608413383Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:21.608419237Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:21.608425253Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:21.608431341Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:21.608437468Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:21.608442961Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:21.608448579Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:21.608455350Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:21.608467303Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:21.608473863Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:21.608480391Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:21.608486043Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:21.608492242Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:21.608497763Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:21.608504036Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:21.608509611Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:21.608517663Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:21.609867031Z [err]  [2026-03-12 17:26:21 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:21.609934493Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:21.609942041Z [err]      І `Procfile`:
2026-03-12T17:26:21.609948357Z [err]        ^
2026-03-12T17:26:21.609954999Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:21.609960566Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:21.609979106Z [err]  [2026-03-12 17:26:21 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:21.609987121Z [err]  [2026-03-12 17:26:21 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:21.609993377Z [err]  [2026-03-12 17:26:21 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:22.201097526Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:22.201104274Z [err]      І `Procfile`:
2026-03-12T17:26:22.201110511Z [err]        ^
2026-03-12T17:26:22.201117597Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:22.572363477Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:22.572380900Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:22.572393687Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:22.572394950Z [err]  Traceback (most recent call last):
2026-03-12T17:26:22.572401793Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:22.572405566Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:22.572408727Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:22.572424790Z [err]      worker.init_process()
2026-03-12T17:26:22.572432075Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:22.572440486Z [err]      self.load_wsgi()
2026-03-12T17:26:22.572448639Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:22.572457149Z [err]  [2026-03-12 17:26:22 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:22.572458543Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:22.572465597Z [err]  [2026-03-12 17:26:22 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:22.572467712Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:22.572474385Z [err]  [2026-03-12 17:26:22 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:22.572476660Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:22.572482926Z [err]  [2026-03-12 17:26:22 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:22.572485761Z [err]      self.callable = self.load()
2026-03-12T17:26:22.572490952Z [err]  [2026-03-12 17:26:22 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:22.572497724Z [err]  [2026-03-12 17:26:22 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:22.574038160Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:22.574048656Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:22.574049512Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:22.574056224Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:22.574062404Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:22.574065404Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:22.574072950Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:22.574080571Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:22.574087181Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:22.574094381Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:22.574095606Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:22.574104621Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:22.574108952Z [err]      І `Procfile`:
2026-03-12T17:26:22.574113176Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:22.574119504Z [err]        ^
2026-03-12T17:26:22.574121807Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:22.574131384Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:22.574137781Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:22.574148147Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:22.574154464Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:22.574161152Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:22.575627684Z [err]  [2026-03-12 17:26:22 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:22.575639399Z [err]  [2026-03-12 17:26:22 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:22.575649267Z [err]  [2026-03-12 17:26:22 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:22.575758806Z [err]  [2026-03-12 17:26:22 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:23.078266373Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:23.078274719Z [err]      І `Procfile`:
2026-03-12T17:26:23.078280684Z [err]        ^
2026-03-12T17:26:23.078287025Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:23.187490155Z [err]  [2026-03-12 17:26:23 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:23.187498742Z [err]  [2026-03-12 17:26:23 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:23.187505781Z [err]  [2026-03-12 17:26:23 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:23.201822047Z [err]  [2026-03-12 17:26:23 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:23.203545192Z [err]  [2026-03-12 17:26:23 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:23.210208551Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:23.210221230Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:23.210229010Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:23.210236245Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:23.210244652Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:23.210251320Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:23.210268621Z [err]  [2026-03-12 17:26:23 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:23.210277247Z [err]  Traceback (most recent call last):
2026-03-12T17:26:23.210283292Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:23.210292887Z [err]      worker.init_process()
2026-03-12T17:26:23.210298570Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:23.210304263Z [err]      self.load_wsgi()
2026-03-12T17:26:23.210310963Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:23.210316835Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:23.210324967Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:23.210330626Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:23.210336336Z [err]      self.callable = self.load()
2026-03-12T17:26:23.210341675Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:23.210347494Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:23.210353007Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:23.210361110Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:23.211951407Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:23.211962836Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:23.211970239Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:23.211977141Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:23.211983135Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:23.211991957Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:23.211996667Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:23.212003493Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:23.212008913Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:23.212014240Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:23.212019421Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:23.212025780Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:23.212030461Z [err]      І `Procfile`:
2026-03-12T17:26:23.212035275Z [err]        ^
2026-03-12T17:26:23.212039485Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:23.212043847Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:23.212049129Z [err]  [2026-03-12 17:26:23 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:23.599662241Z [err]  [2026-03-12 17:26:23 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:23.599675020Z [err]  [2026-03-12 17:26:23 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:23.599683643Z [err]  [2026-03-12 17:26:23 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:23.894975611Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:23.894983443Z [err]      І `Procfile`:
2026-03-12T17:26:23.894989558Z [err]        ^
2026-03-12T17:26:23.894994840Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:24.012693185Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:24.012706346Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:24.012714054Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:24.044616279Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:24.044622600Z [err]  [2026-03-12 17:26:24 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:24.044628524Z [err]  [2026-03-12 17:26:24 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:24.044634166Z [err]  Traceback (most recent call last):
2026-03-12T17:26:24.044640080Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:24.044646161Z [err]      worker.init_process()
2026-03-12T17:26:24.044651700Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:24.044658097Z [err]      self.load_wsgi()
2026-03-12T17:26:24.044663865Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:24.044670057Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:24.044675971Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:24.044682010Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:24.044688435Z [err]      self.callable = self.load()
2026-03-12T17:26:24.044695778Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:24.044701852Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:24.044707706Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:24.044713514Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:24.044719494Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:24.044725204Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:24.044730950Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:24.044736574Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:24.046772951Z [err]  [2026-03-12 17:26:24 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:24.046794978Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:24.046805795Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:24.046812740Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:24.046819964Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:24.046826340Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:24.046832212Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:24.046838048Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:24.046843854Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:24.046850569Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:24.046858840Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:24.046863614Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:24.046868031Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:24.046872042Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:24.046876197Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:24.046880457Z [err]      І `Procfile`:
2026-03-12T17:26:24.046885181Z [err]        ^
2026-03-12T17:26:24.046889221Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:24.046894743Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:24.119900916Z [err]  [2026-03-12 17:26:24 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:24.119916999Z [err]  [2026-03-12 17:26:24 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:24.119925987Z [err]  [2026-03-12 17:26:24 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:24.886998284Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:24.887004262Z [err]      І `Procfile`:
2026-03-12T17:26:24.887020593Z [err]        ^
2026-03-12T17:26:24.887026753Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:24.999180130Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:24.999187711Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:24.999194382Z [err]  [2026-03-12 17:26:24 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:25.020383605Z [err]  [2026-03-12 17:26:25 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:25.020391002Z [err]  [2026-03-12 17:26:25 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:25.031419074Z [err]      self.callable = self.load()
2026-03-12T17:26:25.031429567Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:25.031438222Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:25.031446169Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:25.031451945Z [err]  [2026-03-12 17:26:25 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:25.031455635Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:25.031462149Z [err]  Traceback (most recent call last):
2026-03-12T17:26:25.031464287Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:25.031470772Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:25.031473803Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:25.031477460Z [err]      worker.init_process()
2026-03-12T17:26:25.031484159Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:25.031484246Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:25.031493136Z [err]      self.load_wsgi()
2026-03-12T17:26:25.031494893Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:25.031499493Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:25.031504117Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:25.031507022Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:25.031513795Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:25.031513902Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:25.031522389Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:25.033198625Z [err]        ^
2026-03-12T17:26:25.033201252Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:25.033208161Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:25.033215321Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:25.033215859Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:25.033230206Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:25.033236030Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:25.033237138Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:25.033242793Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:25.033247889Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:25.033252672Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:25.033258781Z [err]  [2026-03-12 17:26:25 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:25.033260871Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:25.033266911Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:25.033271451Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:25.033276724Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:25.033281596Z [err]      І `Procfile`:
2026-03-12T17:26:25.106326728Z [err]  [2026-03-12 17:26:25 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:25.108101492Z [err]  [2026-03-12 17:26:25 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:25.108109852Z [err]  [2026-03-12 17:26:25 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:25.875024058Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:25.875030041Z [err]      І `Procfile`:
2026-03-12T17:26:25.875034870Z [err]        ^
2026-03-12T17:26:25.875039974Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:26.004605946Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:26.004610826Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:26.004615566Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:26.031913443Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:26.031921674Z [err]  [2026-03-12 17:26:26 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:26.042658557Z [err]  [2026-03-12 17:26:26 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:26.042665079Z [err]  Traceback (most recent call last):
2026-03-12T17:26:26.042670732Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:26.042678576Z [err]      worker.init_process()
2026-03-12T17:26:26.042684390Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:26.042689160Z [err]      self.load_wsgi()
2026-03-12T17:26:26.042694646Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:26.042699692Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:26.042704887Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:26.042710902Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:26.042716500Z [err]      self.callable = self.load()
2026-03-12T17:26:26.042722257Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:26.042735616Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:26.042742123Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:26.042747788Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.042753716Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:26.042760708Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:26.042766903Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.042773816Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:26.042780482Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:26.042788107Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.044534208Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:26.044538219Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:26.044548148Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:26.044554127Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:26.044558441Z [err]  [2026-03-12 17:26:26 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:26.044567815Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.044580308Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:26.044588842Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:26.044596788Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:26.044604270Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:26.044611407Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:26.044619134Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:26.044626531Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:26.044633528Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:26.044640713Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:26.044647977Z [err]      І `Procfile`:
2026-03-12T17:26:26.044654867Z [err]        ^
2026-03-12T17:26:26.085927480Z [err]  [2026-03-12 17:26:26 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:26.085933368Z [err]  [2026-03-12 17:26:26 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:26.085939480Z [err]  [2026-03-12 17:26:26 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:26.772399594Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:26.772403884Z [err]      І `Procfile`:
2026-03-12T17:26:26.772408864Z [err]        ^
2026-03-12T17:26:26.772413147Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:26.884390210Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:26.884403954Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:26.884411747Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:26.921079359Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:26.921092364Z [err]      self.callable = self.load()
2026-03-12T17:26:26.921098323Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:26.921103511Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:26.921109355Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:26.921115137Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.921120397Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:26.921125279Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:26.921129761Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.921136175Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:26.921140051Z [err]  [2026-03-12 17:26:26 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:26.921149448Z [err]  [2026-03-12 17:26:26 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:26.921156475Z [err]  [2026-03-12 17:26:26 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:26.921162357Z [err]  Traceback (most recent call last):
2026-03-12T17:26:26.921168297Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:26.921174571Z [err]      worker.init_process()
2026-03-12T17:26:26.921182075Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:26.921189192Z [err]      self.load_wsgi()
2026-03-12T17:26:26.921194897Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:26.921200728Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:26.921206657Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:26.923148884Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:26.923157038Z [err]      І `Procfile`:
2026-03-12T17:26:26.923162626Z [err]        ^
2026-03-12T17:26:26.923167824Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:26.923172661Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:26.923177794Z [err]  [2026-03-12 17:26:26 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:26.923197289Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:26.923211570Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.923219827Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:26.923227062Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:26.923236174Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:26.923243109Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:26.923249277Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:26.923255910Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:26.923262066Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:26.923269261Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:26.923276008Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:26.923281957Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:26.923288707Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:26.958430362Z [err]  [2026-03-12 17:26:26 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:26.960356110Z [err]  [2026-03-12 17:26:26 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:26.960366259Z [err]  [2026-03-12 17:26:26 +0000] [5] [ERROR] Reason: Worker failed to boot.
2026-03-12T17:26:27.666354771Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:27.666363457Z [err]      І `Procfile`:
2026-03-12T17:26:27.666370007Z [err]        ^
2026-03-12T17:26:27.666378479Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:27.801373455Z [err]  [2026-03-12 17:26:27 +0000] [5] [INFO] Starting gunicorn 25.1.0
2026-03-12T17:26:27.801377866Z [err]  [2026-03-12 17:26:27 +0000] [5] [INFO] Listening at: http://0.0.0.0:8080 (5)
2026-03-12T17:26:27.801383666Z [err]  [2026-03-12 17:26:27 +0000] [5] [INFO] Using worker: sync
2026-03-12T17:26:27.827905084Z [err]  [2026-03-12 17:26:27 +0000] [5] [INFO] Control socket listening at /app/gunicorn.ctl
2026-03-12T17:26:27.827911824Z [err]  [2026-03-12 17:26:27 +0000] [7] [INFO] Booting worker with pid: 7
2026-03-12T17:26:27.838655250Z [err]  [2026-03-12 17:26:27 +0000] [7] [ERROR] Exception in worker process
2026-03-12T17:26:27.838662169Z [err]  Traceback (most recent call last):
2026-03-12T17:26:27.838667812Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/arbiter.py", line 708, in spawn_worker
2026-03-12T17:26:27.838673922Z [err]      worker.init_process()
2026-03-12T17:26:27.838679858Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 136, in init_process
2026-03-12T17:26:27.838685974Z [err]      self.load_wsgi()
2026-03-12T17:26:27.838691599Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/workers/base.py", line 148, in load_wsgi
2026-03-12T17:26:27.838697215Z [err]      self.wsgi = self.app.wsgi()
2026-03-12T17:26:27.838701830Z [err]                  ^^^^^^^^^^^^^^^
2026-03-12T17:26:27.838706420Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/base.py", line 66, in wsgi
2026-03-12T17:26:27.838711595Z [err]      self.callable = self.load()
2026-03-12T17:26:27.838716044Z [err]                      ^^^^^^^^^^^
2026-03-12T17:26:27.838720440Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 57, in load
2026-03-12T17:26:27.838724802Z [err]      return self.load_wsgiapp()
2026-03-12T17:26:27.838729980Z [err]             ^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:27.838734707Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 47, in load_wsgiapp
2026-03-12T17:26:27.838739058Z [err]      return util.import_app(self.app_uri)
2026-03-12T17:26:27.838745627Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:27.838751464Z [err]    File "/opt/venv/lib/python3.12/site-packages/gunicorn/util.py", line 377, in import_app
2026-03-12T17:26:27.838757636Z [err]      mod = importlib.import_module(module)
2026-03-12T17:26:27.838763064Z [err]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:27.841754619Z [err]    File "/root/.nix-profile/lib/python3.12/importlib/__init__.py", line 90, in import_module
2026-03-12T17:26:27.841763105Z [err]      return _bootstrap._gcd_import(name[level:], package, level)
2026-03-12T17:26:27.841771530Z [err]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-03-12T17:26:27.841779013Z [err]    File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2026-03-12T17:26:27.841787333Z [err]    File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2026-03-12T17:26:27.841793210Z [err]    File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2026-03-12T17:26:27.841801445Z [err]    File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2026-03-12T17:26:27.841815308Z [err]    File "<frozen importlib._bootstrap_external>", line 991, in exec_module
2026-03-12T17:26:27.841822400Z [err]    File "<frozen importlib._bootstrap_external>", line 1129, in get_code
2026-03-12T17:26:27.841828533Z [err]    File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
2026-03-12T17:26:27.841834543Z [err]    File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2026-03-12T17:26:27.841842977Z [err]    File "/app/bot.py", line 72
2026-03-12T17:26:27.841849896Z [err]      І `Procfile`:
2026-03-12T17:26:27.841856518Z [err]        ^
2026-03-12T17:26:27.841862285Z [err]  SyntaxError: invalid syntax
2026-03-12T17:26:27.841868657Z [err]  invalid syntax (bot.py, line 72)
2026-03-12T17:26:27.841874874Z [err]  [2026-03-12 17:26:27 +0000] [7] [INFO] Worker exiting (pid: 7)
2026-03-12T17:26:27.911744427Z [err]  [2026-03-12 17:26:27 +0000] [5] [ERROR] Worker (pid:7) exited with code 3.
2026-03-12T17:26:27.914279725Z [err]  [2026-03-12 17:26:27 +0000] [5] [ERROR] Shutting down: Master
2026-03-12T17:26:27.914285392Z [err]  [2026-03-12 17:26:27 +0000] [5] [ERROR] Reason: Worker failed to boot.
