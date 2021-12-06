import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthServiceService } from '../auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.sass']
})
export class SearchComponent implements OnInit {

  type = 'movie'
  res:any
  search:boolean = false
  ml:any

  att = new FormGroup({
    attraction: new FormControl('')
  });

  constructor(private service: AuthServiceService, private router: Router) { }

  ngOnInit(): void {

  }
  

  async onSubmit(){
    console.log(this.att.value.attraction)
    try{
      this.res = await this.service.search(this.att.value.attraction, this.type)
    }catch(error){
      console.log(error)
    }
    
    console.log(this.res)
    this.res = this.res.data
    this.search = false
  }
  gosta:any
  async onClick(title:any,id:any){
    window.localStorage.setItem('id',id)
    this.search = true
    console.log(title)
    this.ml = await this.service.mlGet(title)
    this.ml = this.ml.data
    this.gosta = this.ml[1] * 100


    console.log(this.ml)
  }

  changeType(tp:any){
    this.type = tp
  }
}
