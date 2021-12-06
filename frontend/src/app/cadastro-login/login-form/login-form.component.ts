import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthServiceService } from 'src/app/auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.sass']
})
export class LoginFormComponent implements OnInit {

  user = new FormGroup({
    username: new FormControl(''),
    password: new FormControl('')
  });


  constructor(private service: AuthServiceService,
    private router: Router ) { }


  async onSubmit(){
    try{
      const result = await this.service.login(this.user);
      console.log(result);
      const token = window.localStorage.getItem('token')
      //const ml = await this.service.mlPost(token)
      //console.log(ml)
      this.router.navigate([''])
    }catch(error){
      console.log(error)
    }
    
  }

  ngOnInit(): void {
  }

}
