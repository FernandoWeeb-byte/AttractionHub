import { Component, OnInit, Input } from '@angular/core';
import { faPowerOff } from '@fortawesome/free-solid-svg-icons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header-logged',
  templateUrl: './header-logged.component.html',
  styleUrls: ['./header-logged.component.sass']
})
export class HeaderLoggedComponent implements OnInit {
  faPowerOff = faPowerOff;
  constructor(private service: Router) { }
  @Input() user:any
  ngOnInit(): void {
  }
  logOut(){
    window.localStorage.removeItem('token')
    this.service.navigate(['login'])

  }
}
