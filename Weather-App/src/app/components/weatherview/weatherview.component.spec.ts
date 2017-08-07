import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeatherviewComponent } from './weatherview.component';

describe('WeatherviewComponent', () => {
  let component: WeatherviewComponent;
  let fixture: ComponentFixture<WeatherviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeatherviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeatherviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
