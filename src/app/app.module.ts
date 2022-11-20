import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FetchDataComponent } from './fetch-data/fetch-data.component';
import { AboutComponent } from './about/about.component';
import { GasMapComponent } from './gas-map/gas-map.component';

import { HttpClientModule } from '@angular/common/http';

import { environment } from 'src/environments/environment';

@NgModule({
  declarations: [
    AppComponent,
    FetchDataComponent,
    AboutComponent,
    GasMapComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]

})
export class AppModule { }



