import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginTelaComponent } from './cadastro-login/login-tela/login-tela.component';
import { CadastroTelaComponent } from './cadastro-login/cadastro-tela/cadastro-tela.component';
import { HomeComponent } from './home/home.component';
const routes: Routes = [
  {path: '', component: HomeComponent },
  {path: 'cadastro', component: CadastroTelaComponent},
  {path: 'login', component: LoginTelaComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
