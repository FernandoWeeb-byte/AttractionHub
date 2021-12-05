import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthServiceService } from 'src/app/auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cadastro-form',
  templateUrl: './cadastro-form.component.html',
  styleUrls: ['./cadastro-form.component.sass']
})
export class CadastroFormComponent implements OnInit {

  user = new FormGroup({
    name: new FormControl(''),
    username: new FormControl(''),
    email: new FormControl(''),
    password: new FormControl('')
  });

  constructor(private service: AuthServiceService,
    private router: Router) { }

  async onSubmit(){
    try{
      const result = await this.service.create(this.user);
      this.router.navigate(['login'])
      console.log(result)
    } catch(error){
      console.error(error)
    }
  }

  ngOnInit(): void {
  }

}
