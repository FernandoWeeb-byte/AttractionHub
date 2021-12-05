import { Component, OnInit,Input } from '@angular/core';
import { AuthServiceService } from 'src/app/auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-attraction',
  templateUrl: './attraction.component.html',
  styleUrls: ['./attraction.component.sass']
})
export class AttractionComponent implements OnInit {

  constructor(private service: AuthServiceService, private router: Router) { }

 
  id:any
  att:any
  async ngOnInit(): Promise<void> {
    this.id = window.localStorage.getItem('id')
    try{
      this.att = await this.service.searchId(this.id)
    }catch(error){
      console.log(error)
    }
    
    console.log(this.att)
    this.att = this.att.data
    console.log(this.att)
    
  }

  res:any
  async onClick(){
    try{
      this.res = await this.service.addToList(this.att)
    }catch(error){
      console.log(error)
    }
    this.router.navigate(['list'])
  }

}
