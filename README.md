### Congress map 


# Idea
MVP
Interactive map that allows you to easily put in your address and find the congressional district and your rep

Miro board: https://miro.com/app/board/uXjVGbsUf0w=/


# TODO:

flask has water running through it.  MapJs library? for a fun frontend  with vite for the dev server?

to deploy i think building react as static files? and then serve w/ flask; running flask with gunicorn 

[A beginners guide to using Vite React](https://codeparrot.ai/blogs/a-beginners-guide-to-using-vite-react)

[MapLibre GL JS](https://maplibre.org/maplibre-gl-js/docs/)

for local dev mount the flask server to /api

```js
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        changeOrigin: true,
      },
    },
  },
});
```


GOALS
AI summary of congresspersons voting record/ policies 
News feed related to your congressional district


FAR Goals:
election tracking and reporting? 



Sources:
Mix of scrapers and public apis 

api.congress.gov: [Congress.gov API]("https://api.congress.gov/#/amendments")
Account Email: max@razorbill.com

# git hub (i can just do better to make a wrapper around the api )
[GitHub - LibraryOfCongress/api.congress.gov: congress.gov API](https://github.com/LibraryOfCongress/api.congress.gov) 
# address -> congressional district:
https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html



Civic info api (elections and voter info )
https://developers.google.com/civic-information/docs/v2


Mapping api for getting the GIS data: (ideally for front end)
https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Legislative/MapServer




Misc: 
vscode run current file from root dir: launch.json:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug: Current File",
            "type": "debugpy",
            "request": "launch", 
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "justMyCode": false,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        },
    ]
}
```

Utils: t.dig() for typesafe dict access 
ex:


