# Scale-factor-evolution

$\textbf{I - Friedmann's equations}$

In this paper, I won't do the derivation from the Einstein field equations $R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu} + \Lambda g_{\mu \nu} = \frac{8 \pi G}{c^4} T_{\mu \nu}$ to the Friedmann's equations :

$$(1) ~~~~~~~~ \frac{\dot{a}^2}{a^2} = \frac{8 \pi G}{3} \rho - \frac{k}{a^2} + \frac{\Lambda}{3}$$

$$(2) ~~~~~~~~ \frac{\ddot{a}}{a} = - \frac{4 \pi G}{3} (\rho + 3P) + \frac{\Lambda}{3}$$

but we also can specify the law of continuity : $\dot{\rho} = -3 \frac{\dot{a}}{a}(\rho + P) ~~~~~~ (3)$

So from these equations, we're going to compute the numerical solution from a differential equation we're going to derivate.

We also can consider others parameters such as the Hubble constant : $H_0 = H(0) = \frac{\dot{a}(0)}{a(0)}$,

the deceleration parameter $q_0 = q(0) = \big( \frac{\ddot{a}a}{\dot{a}^2} \big )_0$ 

and the critical density $\rho_c(0) = \rho_{c,0} = \frac{3 H_0^2}{8 \pi G}$

$\textbf{II - Content components of the Universe}$

For a Universe mainly constitutes of a certain content, the evolution of the scale factor will be given by their state equations.

- for the matter : $\Omega_0^M = \frac{\rho_M(0)}{\rho_{0,c}} \to \rho_M(t) \propto a(t)^{-3}$
- for the radiation : $\Omega_0^R = \frac{\rho_R(0)}{\rho_{0,c}} \to \rho_R(t) \propto a(t)^{-4}$
- for the dark energy : $\Omega_0^{\Lambda} = \frac{\rho_{\Lambda}(0)}{\rho_{0,c}} = \frac{\Lambda c^2}{3H_0^2} \to \rho_{\Lambda}(t) \propto e^{\sqrt{\frac{\Lambda}{3}t}}$

Let’s start with the first Friedmann equation (written in terms of the Hubble parameter now).

$$H^2(t) = \frac{8\pi G}{3} \bigg( \rho(t) - \frac{3k}{8\pi G a^2(t)} \bigg ) $$

But $\rho(t) \gg \frac{3k}{8\pi G a^2(t)}$ so we can consider that $H^2(t) = \frac{8\pi G}{3} \rho(t)$ and we remember that $\Omega = \frac{\rho(t)}{\rho_c} = \frac{8 \pi G \rho(t)}{3 H^2_0}$.

We can rearrange $\Omega_M =  \frac{8 \pi G}{3 H^2_0} \rho_M(t) = \frac{\rho_M(t)}{\rho_{0,c}} = \frac{\rho_M(t)}{\rho_M(t_0)} \frac{\rho_M(t_0)}{\rho_{0,c}} = a^{-3}(t)\Omega_{M,0} = \Omega_{M,0} a^{-3}(t)$.

Then, $\rho_M(t) = \frac{3 H_0^2}{8 \pi G}\Omega_{M,0} a^{-3}(t)$ and we can do the same for the other consituants : 

$\rho_R(t) = \frac{3 H_0^2}{8 \pi G}\Omega_{R,0} a^{-4}(t)$

$\rho_k(t) = \frac{3 H_0^2}{8 \pi G}\Omega_{k,0} a^{-2}(t)$

$\rho_{\Lambda}(t) = \frac{3 H_0^2}{8 \pi G}\Omega_{\Lambda}$

So, as $H^2(t) = \frac{8\pi G}{3} \rho(t) \to H^2(t) = H_0^2\frac{8\pi G}{3H_0^2} \big (\rho_M(t) + \rho_R(t) +  \rho_k(t) + \rho_{\Lambda}(t) \big )$

$$H(t)^2 = H_0^2 \frac{1}{\rho_c} \big (\rho_M(t) + \rho_R(t) +  \rho_k(t) + \rho_{\Lambda}(t)\big )$$

$$H(t)^2 = H_0^2 \frac{1}{\rho_c} \big (\Omega_{M,0} a^{-3}(t) + \Omega_{R,0} a^{-4}(t) +  \Omega_{k,0} a^{-2}(t) + \Omega_{\Lambda} \big )$$

 $\textbf{III - Equations and numerical solving}$ 
$\textbf{(1)}$ and (2) $\textbf{(2)}$ involve the first and second derivative of the scale factor. The aim is to combine these two equations to obtain a second order differential equation in matrix form. We introduce the normalized scale factor $\tilde{a}(t) = \frac{a(t)}{a_0}$. 

$\textbf{(1)}$ can be written as :

$$(4) ~~~~~~~~ \ddot{\tilde{a}} = - \frac{1}{2} \tilde{a} H_0^2 \Bigg( \frac{\Omega_{M,0}}{\tilde{a}^3} +2 \frac{\Omega_{R,0}}{\tilde{a}^4} -2\Omega_{\Lambda,0} \Bigg)$$

and $\textbf{(2)}$ :

$$ (5) ~~~~~~~~ \tilde{a} = \Omega_{M,0} \Bigg( \frac{\dot{\tilde{a}}^2}{H_0^2} - \frac{\Omega_{R,0}}{\tilde{a}^2} -\tilde{a}^2 \Omega_{\Lambda,0} - \Omega_{k,0}\Bigg)^{-1}$$

Where $\Omega_{M,0} + \Omega_{R,0} + \Omega_{\Lambda,0} + \Omega_{k,0} = 1$

We inject the 2 new equations $\textbf{(4)}$ and $\textbf{(5)}$ into each other to obtain a new differential equation describing the evolution of the normalised scale factor :

$$ \ddot{\tilde{a}} = - \frac{1}{2} \Omega_{M,0} \Bigg( \frac{\dot{\tilde{a}}^2}{H_0^2} - \frac{\Omega_{R,0}}{\tilde{a}^2} -\tilde{a}^2 \Omega_{\Lambda,0} - \Omega_{k,0}\Bigg)^{-1} H_0^2 \Bigg( \frac{\Omega_{M,0}}{\tilde{a}^3} +2 \frac{\Omega_{R,0}}{\tilde{a}^4} -2\Omega_{\Lambda,0} \Bigg)$$

This ODE can be easily solved with the library $\textit{scipy.integrate}$ and in the code, this ODE is given by the function :

    def syseq(y, t, Omega_m, Omega_r, Omega_l, Omega_k, H0):
        dydt = [y[1],
                (-(H0 ** 2 / 2) * (Omega_m / y[0] ** 3 + 2 * Omega_r / y[0] ** 4 - 2 * Omega_l)) * Omega_m * (
                            1 / (H0 ** 2) * y[1] ** 2 -
                            Omega_r / y[0] ** 2 - Omega_l * y[0] ** 2 - Omega_k) ** (-1)]
        return dydt

And we can plot it for several values of $\Omega_{M}, \Omega_{\Lambda}$ etc. According to the articles from $\textit{Planck 2018}$ and $\textit{SH0ES 2022}$ the cosmological values constraint $\tilde{a}$ :

![image](https://github.com/user-attachments/assets/84a8f641-a91b-49d2-9b20-f0932d749052)

