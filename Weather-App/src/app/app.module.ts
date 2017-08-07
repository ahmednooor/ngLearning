import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { WeatherviewComponent } from './components/weatherview/weatherview.component';
import { SearchComponent } from './components/search/search.component';

import { GetweatherService } from './services/getweather/getweather.service';

@NgModule({
  declarations: [
    AppComponent,
    WeatherviewComponent,
    SearchComponent
  ],
  imports: [
    BrowserModule,
    HttpModule
  ],
  providers: [
    GetweatherService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
