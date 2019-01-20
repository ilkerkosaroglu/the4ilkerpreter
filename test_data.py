# All test cases created by Burak Akkaya
FS001 = ["/", "d",
         ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
         ["home", "d",
          ["psychology", "d", ["trauma", "d", ["pills.py", "f"], ["coffee.jpg", "f"]], ["versus.py", "f"],
           ["crazy", "d", ["stars.jpg", "f"], ["custody.avi", "f"]]],
          ["street", "d", ["ritman.py", "f"], ["future.txt", "f"], ["jfd", "d"]]]]
C001 = ["cd home/psychology/",
        "mkdir ../psychology/crazy/prison",
        "rmdir /home/./street/jfd",
        "cd .././..//studio",
        "rm ../home/psychology/versus.py",
        "cp zero.py /home/"]
R001 = ("SUCCESS", ["/", "d",
                    ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
                    ["home", "d",
                     ["psychology", "d", ["trauma", "d", ["pills.py", "f"], ["coffee.jpg", "f"]],
                      ["crazy", "d", ["stars.jpg", "f"], ["custody.avi", "f"], ["prison", "d"]]],
                     ["street", "d", ["ritman.py", "f"], ["future.txt", "f"]], ["zero.py", "f"]]], "/studio")

FS002 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C002 = ["cd series/netflix",
        "rmdir .././/../musics/ajdar",
        "cd .."]
R002 = ("ERROR", "rmdir .././/../musics/ajdar", "/series/netflix")

FS003 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C003 = ["cd series/netflix",
        "exec black.avi",
        "exec /musics/ajdar/turpgibi.mp3",
        "rm ../..//movies/2018",
        "cd /movies/2018"]
R003 = ("ERROR", "rm ../..//movies/2018", "/series/netflix")

FS004 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C004 = ["cd photos",
        "rm ../series/netflix/black.avi",
        "cp /movies/2010 ../musics/",
        "exec /series/netflix/mirror.mkv"]
R004 = ("ERROR", "cp /movies/2010 ../musics/", "/photos")

FS005 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C005 = ["cd musics/tarkan",
        "rmdir ../.././//./musics/2010"]
R005 = ("SUCCESS", ["/", "d",
                    ["movies", "d", ["2018", "d"], ["2010", "d"]],
                    ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
                    ["photos", "d"],
                    ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"]]], "/musics/tarkan")

FS006 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C006 = ["exec movies/2018"]
R006 = ("ERROR", "exec movies/2018", "/")

FS007 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C007 = ["cd software",
        "mkdir ../games/finished",
        "cp valecnikrpg /games/finished/",
        "cd ..//games/finished/valecnikrpg"]
R007 = ("SUCCESS", ["/", "d",
                    ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
                    ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
                    ["plans", "d", ["website", "d", ["index.php", "f"]]],
                    ["games", "d", ["finished", "d", ["valecnikrpg", "d", ["main.py", "f"]]]],
                    ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]],
        "/games/finished/valecnikrpg")

FS008 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C008 = ["cd work",
        "cd .../plans",
        "cd ../*"]
R008 = ("ERROR", "cd .../plans", "/work")

FS009 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C009 = ["cd plans/website/index.php"]
R009 = ("ERROR", "cd plans/website/index.php", "/")

FS010 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C010 = ["cd software/valecnikrpg",
        "rmdir ../../work",
        "cd /work"]
R010 = ("ERROR", "rm ../../work", "/software/valecnikrpg")

FS011 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C011 = ["cd plans/*"]
R011 = ("ERROR", "cd plans/*", "/")

FS012 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C012 = ["cd earth",
        "rm .././water/sea"]
R012 = ("ERROR", "rm .././water/sea", "/earth")

FS013 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C013 = ["cd water/sea",
        "rmdir /earth/mountain.jpg"]
R013 = ("ERROR", "rmdir /earth/mountain.jpg", "/water/sea")

FS014 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C014 = ["cd fire",
        "rmdir .."]
R014 = ("ERROR", "rmdir ..", "/fire")

FS015 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C015 = ["cp earth/mountain.jpg /water/sea/",
        "cd earth",
        "rm mountain.jpg",
        "exec ../water/sea/mountain.jpg"]
R015 = ("SUCCESS",
        ['/', 'd', ['fire', 'd'], ['water', 'd', ['sea', 'd', ['mountain.jpg', 'f']], ['lake', 'd']], ['earth', 'd'],
         ['air', 'd']], "/earth")

FS016 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C016 = ["cp the3/the the4",
        "cd the4/the",
        "exec the3.py"]
R016 = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
                    ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
                    ["the4", "d", ["the", "d", ["the3.py", "f"]]]], "/the4/the")

FS017 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d"], ["rules.pdf", "f"]],
         ["the4", "d"]]
C017 = ["rmdir the3/the",
        "cd the2/the"]
R017 = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
                    ["the3", "d", ["rules.pdf", "f"]],
                    ["the4", "d"]], "/the2/the")

FS018 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C018 = ["mkdir the1/the",
        "cd the1/the",
        "mkdir /the3/the"]
R018 = ("ERROR", "mkdir /the3/the", "/the1/the")

FS019 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C019 = ["exec the2/the/first.txt",
        "cd the3",
        "exec the/the3.py",
        "rm ../the2/the"]
R019 = ("ERROR", "rm ../the2/the", "/the3")

FS020 = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d"], ["rules.pdf", "f"]],
         ["the4", "d"]]
C020 = ["cp the3 the2/",
        "rmdir the2/the3/the",
        "cd the2/the/"]
R020 = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]],
                     ["the3", "d", ["rules.pdf", "f"]]],
                    ["the3", "d", ["the", "d"], ["rules.pdf", "f"]],
                    ["the4", "d"]], "/the2/the")

FS021 = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C021 = ["cd secondline/firstcolumn",
        "exec a.txt",
        "rmdir ../../firstline/secondcolumn"]
R021 = ("ERROR", "rmdir ../../firstline/secondcolumn", "/secondline/firstcolumn")

FS022 = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C022 = ["mkdir secondline/firstcolumn/alttable",
        "cp secondline/firstcolumn firstline/firstcolumn"]
R022 = ("SUCCESS", ["/", "d",
                    ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"],
                                        ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"], ["alttable", "d"]]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
                    ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"], ["alttable", "d"]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]], "/")

FS023 = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C023 = ["cd secondline",
        "rmdir firstcolumn"]
R023 = ("ERROR", "rmdir firstcolumn", "/secondline")

FS024 = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C024 = ["cd firstline/secondcolumn",
        "cp a.txt /secondline/",
        "rm a.txt"]
R024 = ("SUCCESS", ["/", "d",
                    ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["secondcolumn", "d", ["b.txt", "f"]]],
                    ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]], ["a.txt", "f"]]],
        "/firstline/secondcolumn")

FS025 = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d"]]]
C025 = ["exec firstline/secondcolumn/a.txt",
        "cd firstline/secondcolumn",
        "rm a.txt",
        "rm b.txt",
        "rmdir /secondline/secondcolumn"]
R025 = ("SUCCESS", ["/", "d",
                    ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
                    ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]],
        "/firstline/secondcolumn")
# All test cases created by Burak Akkaya
FS001y = ["/", "d",
         ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
         ["home", "d",
          ["psychology", "d", ["trauma", "d", ["pills.py", "f"], ["coffee.jpg", "f"]], ["versus.py", "f"],
           ["crazy", "d", ["stars.jpg", "f"], ["custody.avi", "f"]]],
          ["street", "d", ["ritman.py", "f"], ["future.txt", "f"], ["jfd", "d"]]]]
C001y = ["cd home/psychology/",
        "mkdir ../psychology/crazy/prison",
        "rmdir /home/./street/jfd",
        "cd .././..//studio",
        "rm ../home/psychology/versus.py",
        "cp zero.py /home/"]
R001y = ("SUCCESS", ["/", "d",
                    ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
                    ["home", "d",
                     ["psychology", "d", ["trauma", "d", ["pills.py", "f"], ["coffee.jpg", "f"]],
                      ["crazy", "d", ["stars.jpg", "f"], ["custody.avi", "f"], ["prison", "d"]]],
                     ["street", "d", ["ritman.py", "f"], ["future.txt", "f"]], ["zero.py", "f"]]], "/studio")

FS002y = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C002y = ["cd series/netflix",
        "rmdir .././/../musics/ajdar",
        "cd .."]
R002y = ("ERROR", "rmdir .././/../musics/ajdar", "/series/netflix")

FS003y = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C003y = ["cd series/netflix",
        "exec black.avi",
        "exec /musics/ajdar/turpgibi.mp3",
        "rm ../..//movies/2018",
        "cd /movies/2018"]
R003y = ("ERROR", "rm ../..//movies/2018", "/series/netflix")

FS004y = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C004y = ["cd photos",
        "rm ../series/netflix/black.avi",
        "cp /movies/2010 ../musics/",
        "exec /series/netflix/mirror.mkv"]
R004y = ("ERROR", "cp /movies/2010 ../musics/", "/photos")

FS005y = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C005y = ["cd musics/tarkan",
        "rmdir ../.././//./musics/2010"]
R005y = ("SUCCESS", ["/", "d",
                    ["movies", "d", ["2018", "d"], ["2010", "d"]],
                    ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
                    ["photos", "d"],
                    ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"]]], "/musics/tarkan")

FS006y = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turpgibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C006y = ["exec movies/2018"]
R006y = ("ERROR", "exec movies/2018", "/")

FS007y = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C007y = ["cd software",
        "mkdir ../games/finished",
        "cp valecnikrpg /games/finished/",
        "cd ..//games/finished/valecnikrpg"]
R007y = ("SUCCESS", ["/", "d",
                    ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
                    ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
                    ["plans", "d", ["website", "d", ["index.php", "f"]]],
                    ["games", "d", ["finished", "d", ["valecnikrpg", "d", ["main.py", "f"]]]],
                    ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]],
        "/games/finished/valecnikrpg")

FS008y = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C008y = ["cd work",
        "cd .../plans",
        "cd ../*"]
R008y = ("ERROR", "cd .../plans", "/work")

FS009y = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C009y = ["cd plans/website/index.php"]
R009y = ("ERROR", "cd plans/website/index.php", "/")

FS010y = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C010y = ["cd software/valecnikrpg",
        "rmdir ../../work",
        "cd /work"]
R010y = ("ERROR", "rm ../../work", "/software/valecnikrpg")

FS011y = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnikrpg", "d", ["main.py", "f"]]], ["other", "d"]]
C011y = ["cd plans/*"]
R011y = ("ERROR", "cd plans/*", "/")

FS012y = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C012y = ["cd earth",
        "rm .././water/sea"]
R012y = ("ERROR", "rm .././water/sea", "/earth")

FS013y = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C013y = ["cd water/sea",
        "rmdir /earth/mountain.jpg"]
R013y = ("ERROR", "rmdir /earth/mountain.jpg", "/water/sea")

FS014y = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C014y = ["cd fire",
        "rmdir .."]
R014y = ("ERROR", "rmdir ..", "/fire")

FS015y = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C015y = ["cp earth/mountain.jpg /water/sea/",
        "cd earth",
        "rm mountain.jpg",
        "exec ../water/sea/mountain.jpg"]
R015y = ("SUCCESS",
        ['/', 'd', ['fire', 'd'], ['water', 'd', ['sea', 'd', ['mountain.jpg', 'f']], ['lake', 'd']], ['earth', 'd'],
         ['air', 'd']], "/earth")

FS016y = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C016y = ["cp the3/the the4",
        "cd the4/the",
        "exec the3.py"]
R016y = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
                    ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
                    ["the4", "d", ["the", "d", ["the3.py", "f"]]]], "/the4/the")

FS017y = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d"], ["rules.pdf", "f"]],
         ["the4", "d"]]
C017y = ["rmdir the3/the",
        "cd the2/the"]
R017y = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
                    ["the3", "d", ["rules.pdf", "f"]],
                    ["the4", "d"]], "/the2/the")

FS018y = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C018y = ["mkdir the1/the",
        "cd the1/the",
        "mkdir /the3/the"]
R018y = ("ERROR", "mkdir /the3/the", "/the1/the")

FS019y = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d", ["the3.py", "f"]], ["rules.pdf", "f"]],
         ["the4", "d"]]
C019y = ["exec the2/the/first.txt",
        "cd the3",
        "exec the/the3.py",
        "rm ../the2/the"]
R019y = ("ERROR", "rm ../the2/the", "/the3")

FS020y = ["/", "d",
         ["the1", "d"],
         ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]]],
         ["the3", "d", ["the", "d"], ["rules.pdf", "f"]],
         ["the4", "d"]]
C020y = ["cp the3 the2/",
        "rmdir the2/the3/the",
        "cd the2/the/"]
R020y = ("SUCCESS", ["/", "d",
                    ["the1", "d"],
                    ["the2", "d", ["the", "d", ["first.txt", "f"], ["the2.py", "f"]],
                     ["the3", "d", ["rules.pdf", "f"]]],
                    ["the3", "d", ["the", "d"], ["rules.pdf", "f"]],
                    ["the4", "d"]], "/the2/the")

FS021y = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C021y = ["cd secondline/firstcolumn",
        "exec a.txt",
        "rmdir ../../firstline/secondcolumn"]
R021y = ("ERROR", "rmdir ../../firstline/secondcolumn", "/secondline/firstcolumn")

FS022y = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C022y = ["mkdir secondline/firstcolumn/alttable",
        "cp secondline/firstcolumn firstline/firstcolumn"]
R022y = ("SUCCESS", ["/", "d",
                    ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"],
                                        ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"], ["alttable", "d"]]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
                    ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"], ["alttable", "d"]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]], "/")

FS023y = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C023y = ["cd secondline",
        "rmdir firstcolumn"]
R023y = ("ERROR", "rmdir firstcolumn", "/secondline")

FS024y = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]]
C024y = ["cd firstline/secondcolumn",
        "cp a.txt /secondline/",
        "rm a.txt"]
R024y = ("SUCCESS", ["/", "d",
                    ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["secondcolumn", "d", ["b.txt", "f"]]],
                    ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]], ["a.txt", "f"]]],
        "/firstline/secondcolumn")

FS025y = ["/", "d",
         ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
         ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
          ["secondcolumn", "d"]]]
C025y = ["exec firstline/secondcolumn/a.txt",
        "cd firstline/secondcolumn",
        "rm a.txt",
        "rm b.txt",
        "rmdir /secondline/secondcolumn"]
R025y = ("SUCCESS", ["/", "d",
                    ["firstline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]],
                     ["secondcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]],
                    ["secondline", "d", ["firstcolumn", "d", ["a.txt", "f"], ["b.txt", "f"]]]],
        "/firstline/secondcolumn")
