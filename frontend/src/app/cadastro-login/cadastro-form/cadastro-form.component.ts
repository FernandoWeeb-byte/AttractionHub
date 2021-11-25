import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthServiceService } from 'src/app/auth-service.service';

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

  constructor(private service: AuthServiceService) { }

  onSubmit(){
    this.service.create(this.user).subscribe(
      success => console.log('sucesso')
    )
  }

  ngOnInit(): void {
  }

}
