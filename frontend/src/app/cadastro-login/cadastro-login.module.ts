import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { CadastroFormComponent } from './cadastro-form/cadastro-form.component';
import { CadastroTelaComponent } from './cadastro-tela/cadastro-tela.component';
import {MatButtonModule} from '@angular/material/button'
import {MatInputModule} from '@angular/material/input';
import { LoginTelaComponent } from './login-tela/login-tela.component';
import { LoginFormComponent } from './login-form/login-form.component';
import { AppRoutingModule } from '../app-routing.module';



@NgModule({
  declarations: [
    HeaderComponent,
    CadastroFormComponent,
    CadastroTelaComponent,
    LoginTelaComponent,
    LoginFormComponent
  ],
  imports: [
    CommonModule,
    MatButtonModule,
    MatInputModule,
    AppRoutingModule
  ], 
  exports: [
    CadastroTelaComponent,
    LoginTelaComponent,
    HeaderComponent
    
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA]
})
export class CadastroLoginModule { }
