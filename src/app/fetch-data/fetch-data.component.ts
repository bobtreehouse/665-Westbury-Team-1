import { Component, OnInit } from '@angular/core';


import { environment } from 'src/environments/environment';
import { State, gasAttributesMapping } from './fetch-data.model';


@Component({
  selector: 'app-fetch-data',
  templateUrl: './fetch-data.component.html',
  styleUrls: ['./fetch-data.component.css']
})
export class FetchDataComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }


}
