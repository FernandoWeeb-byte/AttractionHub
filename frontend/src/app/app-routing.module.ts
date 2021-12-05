import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginTelaComponent } from './cadastro-login/login-tela/login-tela.component';
import { CadastroTelaComponent } from './cadastro-login/cadastro-tela/cadastro-tela.component';
import { HomeComponent } from './home/home.component';
import { MyListComponent } from './user/my-list/my-list.component';
import { AttractionComponent } from './user/attraction/attraction.component';


const routes: Routes = [
  {path: '', component: HomeComponent },
  {path: 'cadastro', component: CadastroTelaComponent},
  {path: 'login', component: LoginTelaComponent},
  {path: 'list', component: MyListComponent},
  {path: 'attraction',component: AttractionComponent }
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
