import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/Rx';

@Injectable()
export class GetweatherService {

  constructor(private http: Http) { }

  getWeather(city) {
    return this.http.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=96f8e6150f79484af0ec9186388fa8b0');
  }

}
