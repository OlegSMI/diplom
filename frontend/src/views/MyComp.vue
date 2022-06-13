<template>
  <div ref="maproot"
       style="width: 100%; height: 100%">
  </div>
</template>

<script>
import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile";
// import Image from "ol/layer/Image";
import TileWMS from 'ol/source/TileWMS';
// import ImageWMS from 'ol/source/ImageWMS';
// import Projection from 'ol/proj/Projection';
import Polyline from 'ol/format/Polyline';
import LineString from 'ol/geom/LineString.js';

// import OSM from 'ol/source/OSM'

import VectorSource from 'ol/source/Vector';
import "ol/ol.css";
import { fromLonLat } from 'ol/proj';
// import {
//   Circle as CircleStyle,
//   Fill,
//   Icon,
//   Stroke,
//   Style,
// } from 'ol/style';

import {Vector as VectorLayer} from 'ol/layer';
// import Point from 'ol/geom/Point';
import Feature from 'ol/Feature';

import {
  Stroke,
  Style,
} from 'ol/style';
export default {
    name: 'MapStravaOSM',
    components:{},
    props: {
        points: Array,
        created: Boolean,
        coords: Array,
        // first_coord: Array,
        // user: String,
        // center: {
        //     type: Array,
        //     default: () => { return [59.937, 30.3089] }
        // },

        // zoom:{
        //     type: Number,
        //     default: 30
        // },
    },
    
    data() {
        return {
            currPath:[],
            map: ''
        }
    },
    // watch: {
    //     currPath: {
    //         deep: true,
    //         handler(newValue, oldValue){
    //             console.log('ddvd', newValue);
    //             console.log(oldValue);
    //         }     
    // }
    // },
    mounted() {
        var forest = new TileLayer({
            source: new TileWMS({
                url: 'http://localhost:8100/geoserver/osm/wms',
                params: {
                    tiled: true,
                    "LAYERS": [
                        'osm:forestpark', 
                        'osm:states', 
                        'osm:amenity',
                        'osm:water',
                        'osm:buildings',
                        'osm:roads'
                    ],
                }
            })
        });
        this.map = new Map({
            target: this.$refs.maproot,
            layers: [
                // new TileLayer({
                //     source: new OSM() 
                // }),
                forest
            ],
            view:  new View({
                zoom: 6,
                center: fromLonLat([31, 49]),
            })
        });
    },
    methods:{
        addPolyline(mass){
            for(var i in mass){
                this.currPath.push(fromLonLat(mass[i]))
            }
            console.log(this.currPath)
            var polyline = new Polyline({
                factor: 1e6
            }).writeGeometry(new LineString(this.currPath));

            const route = new Polyline({
            factor: 1e6,
            }).readGeometry(polyline, {
            dataProjection: 'EPSG:4326',
            featureProjection: 'EPSG:3857',
            });



            const styles = {
                'route': new Style({
                    stroke: new Stroke({
                    width: 6,
                    color: [255, 0, 0],
                    }),
                })    
            }

            const routeFeature = new Feature({
            type: 'route',
            geometry: route,
            });

            const vectorLayer = new VectorLayer({
            source: new VectorSource({
                features: [routeFeature],
            }),
            style: function (feature) {
                return styles[feature.get('type')];
            },
            });
            this.map.addLayer(vectorLayer);
            console.log(this.map)
            },
            
    }
}
</script>

