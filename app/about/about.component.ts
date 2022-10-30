import { Component } from '@angular/core';

@Component({
  selector: 'app-about-component',
  templateUrl: './about.component.html'
})
export class CounterComponent {
  public currentCount = 0;

  public incrementCounter() {
    this.currentCount++;
  }
}
