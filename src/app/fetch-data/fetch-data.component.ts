import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { GoogleSheetsDbService } from 'ng-google-sheets-db';

import { environment } from 'src/environments/environment';
import { State, gasAttributesMapping } from './fetch-data.model';


@Component({
  selector: 'app-fetch-data',
  templateUrl: './fetch-data.component.html',
  styleUrls: ['./fetch-data.component.css']
})
export class FetchDataComponent implements OnInit {
  states$!: Observable<State[]>;

  constructor(private googleSheetsDbService: GoogleSheetsDbService) { }

  ngOnInit(): void {
    this.states$ = this.googleSheetsDbService.getActive<State>(
      environment.states.spreadsheetId, environment.states.worksheetName, gasAttributesMapping, 'Active');
  }

}
