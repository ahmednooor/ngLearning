import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-weatherview',
  templateUrl: './weatherview.component.html',
  styleUrls: ['./weatherview.component.css']
})
export class WeatherviewComponent implements OnInit {
  weatherObj:any = {};
  reqSent = false;
  Math = Math

  constructor() { }

  ngOnInit() {
  }

  updateWeatherObj(obj) {
    this.weatherObj = obj;
  }

}
