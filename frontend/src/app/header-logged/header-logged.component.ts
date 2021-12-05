import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-header-logged',
  templateUrl: './header-logged.component.html',
  styleUrls: ['./header-logged.component.sass']
})
export class HeaderLoggedComponent implements OnInit {

  constructor() { }
  @Input() user:any
  ngOnInit(): void {
  }

}
