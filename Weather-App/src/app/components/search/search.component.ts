import { Component, OnInit } from '@angular/core';
import { Response } from '@angular/http';
import 'rxjs/Rx';

import { WeatherviewComponent } from '../weatherview/weatherview.component';

import { GetweatherService } from '../../services/getweather/getweather.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  weatherObj:any = {};

  constructor(private getweatherService: GetweatherService,
              private weatherviewComponent: WeatherviewComponent
  ) { }

  ngOnInit() {
  }

  onSearchSubmit(e, form) {
    e.preventDefault();
    if (form.cityname.value != "") {
      this.weatherviewComponent.reqSent = true;
      this.getweatherService.getWeather(form.cityname.value)
      .subscribe(
        (response: Response) => {
          console.log(response.json())
          this.weatherObj = response.json();
          this.weatherviewComponent.reqSent = false;
          return this.weatherviewComponent.updateWeatherObj(this.weatherObj);
        },
        (error: any) => {
          console.log(error.json())
          this.weatherObj = error.json();
          this.weatherviewComponent.reqSent = false;
          return this.weatherviewComponent.updateWeatherObj(this.weatherObj);
        }
      );
    }
    form.cityname.value = "";
    return false;
  }

}
