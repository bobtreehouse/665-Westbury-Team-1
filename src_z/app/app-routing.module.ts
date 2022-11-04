import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { FetchDataComponent } from './fetch-data/fetch-data.component';
import { AboutComponent } from './about/about.component';
import { GasMapComponent } from './gas-map/gas-map.component';

const routes: Routes = [{ path: '', redirectTo: 'gas-map/', pathMatch: 'full' },
{ path: 'gas-map', component: GasMapComponent },
{ path: 'fetch-data', component: FetchDataComponent },
{ path: 'about', component: AboutComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: []

})
export class AppRoutingModule { }


